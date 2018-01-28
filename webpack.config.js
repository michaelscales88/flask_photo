'use strict';

const webpack = require('webpack'),
      path = require('path');

const config = {
  entry: {
    upload: __dirname + '/app/static/js/upload.js',
  },
  output: {
    path: __dirname + '/app/static/dist',
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
