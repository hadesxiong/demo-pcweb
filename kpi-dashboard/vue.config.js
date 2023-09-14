const { defineConfig } = require('@vue/cli-service');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CompressionPlugin = require('compression-webpack-plugin')

module.exports = defineConfig({
  transpileDependencies: true,
  runtimeCompiler: true,
  configureWebpack: {
    plugins: [
      new MiniCssExtractPlugin(),
      new CompressionPlugin({
        test: /\.(js|css)?$/i,
        algorithm: 'gzip',
        filename: '[path][base].gz',
        minRatio: 1,
        deleteOriginalAssets: false
      })
      // ...other plugins
    ],
  },
})
