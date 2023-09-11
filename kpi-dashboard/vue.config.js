const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  runtimeCompiler: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:3000/api', // 实际 API 地址
        changeOrigin: true,
        pathRewrite: {
          '^/api': '' // 如果您的 API 路径有前缀，可以在此进行重写
        }
      }
    }
  }
})
