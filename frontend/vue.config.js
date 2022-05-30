const BundleTracker = require("webpack-bundle-tracker");

const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
