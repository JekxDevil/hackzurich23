const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  // export the built files in the docs folder
  outputDir: "../electron/build/",
  // change the base path of the app
  publicPath: "./",
});
