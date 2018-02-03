'use strict';
let webpack = require('webpack');
let ExtractTextPlugin = require('extract-text-webpack-plugin');
let path = require('path');


const config = {
  entry: {
    upload: __dirname + '/static/js/upload.jsx',
    gallery: __dirname + '/static/js/gallery.jsx',
  },
  output: { path: __dirname + '/static/dist', filename: "bundle--[name].js" },
  module: {
    loaders: [
      { test: /.jsx?$/, loader: 'babel-loader', query: { presets: ['es2015', 'react', "stage-2"] }, exclude: /node_modules/ },
      { test: /.css?$/, loader: ExtractTextPlugin.extract('style-loader', 'css-loader?modules&importLoaders=1&localIdentName=[name]__[local]___[hash:base64:5]!postcss-loader') }
    ]
  },
  plugins: [
  ]
};

module.exports = config;
