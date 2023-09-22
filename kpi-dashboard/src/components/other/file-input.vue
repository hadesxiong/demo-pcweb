<template>
  <div class="custom-upload">
    <input type="file" style="display: none" ref="fileInput" @change="handleFileChange" />
    <a-upload :show-upload-list="false" :before-upload="beforeUpload" :on-success="onSuccess"
      class="d_flex jc_sb fai_c bg_l2 br_4 ta_l h_32 fc_l2 of_h tover_ell ws_no minw_100 w_240">
      <a-input v-model="fileName" :placeholder="fileName" readonly @click="openFileSelection" class="d_flex fai_c jc_sb p_0 input_file h_32">
        <template #suffix>
          <a @click="cleanFile" class="h_32 lh_32 d_flex fai_c">
            <icon-delete class="lh_1" size="14" fill="#f53f3f" v-if="fileName"></icon-delete>
          </a>
          <a @click="openFileSelection" class="h_32 lh_32 d_flex fai_c">
            <icon-upload class="lh_1 pr_12" size="14" fill="#165dff"></icon-upload>
          </a>
        </template>
      </a-input>
    </a-upload>
  </div>
</template>

<style scoped>
.custom-upload {
  display: inline-block;
}
.ant-input-affix-wrapper {
  background-color: transparent !important;
  text-overflow: ellipsis;
  overflow: hidden;
}

.ant-input-affix-wrapper span {
  width: 100%;
  display: block;
}

.ant-input {
  text-overflow: ellipsis;
  overflow: hidden;
  width: auto;
}
</style>

<style>
.input_file input {
  padding-left: 12px !important;
  line-height: 32px;
}
</style>

<script>
import { defineComponent } from "vue";
import { Delete, Upload as IconUpload } from "@icon-park/vue-next";
import { Upload, Input } from 'ant-design-vue';

export default defineComponent({
  components: {
    'icon-delete': Delete,
    'icon-upload': IconUpload,
    'a-upload': Upload,
    'a-input': Input
  },
  data() {
    return {
      fileName: "",
      uploading: false,
    };
  },
  methods: {
    openFileSelection(event) {
      if (!this.uploading) {
        // 冒泡事件阻止
        event.stopPropagation();
        this.$refs.fileInput.click();
      }
    },
    handleFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.fileName = file.name;
        this.$refs.fileInput.value = ""; // 清空文件选择框的值
      }
      console.log(file)
      this.$emit('file-upload',file);
    },
    beforeUpload(file) {
      // 在上传之前的处理逻辑，例如限制文件类型和大小
      // 返回 false 可以取消上传
      console.log("beforeUpload:", file);
    },
    onSuccess(response, file) {
      // 上传成功后的处理逻辑
      console.log("onSuccess:", response, file);
      this.fileName = file.name; // 将上传成功的文件名展示在输入框中
    },
    cleanFile(event) {
      this.fileName = "";
      event.stopPropagation();
    },
  },
});
</script>
