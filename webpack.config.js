// webpack.config.js
const path = require("path");

module.exports = {
  entry: "./src/index.js", // Replace with your actual entry file
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "dist"),
  },
  mode: "development", // Change to 'production' for production builds
};
