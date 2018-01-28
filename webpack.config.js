'use strict';

const webpack = require('webpack'),
      path = require('path');

let config = {
  entry: {
    index: './app/js/index.js',
  },
  output: {
    path: __dirname + '/app/static',
    filename: "bundle--[name].js"
  },
  module: {
    loaders: [
      {
        test: /\.js?$/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        },
        exclude: /node_modules/
      }
    ]
  },
  plugins: [
  ]
};

module.exports = config;
