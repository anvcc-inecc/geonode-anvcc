/*globals define: true, requirejs: true */

'use strict';

const upload = siteUrl + 'static/geonode/js/upload'
const templates = siteUrl + 'static/geonode/js/templates'

requirejs.config({
  config: {
     text: {
       useXhr: function (url, protocol, hostname, port) {
          // allow cross-domain requests
          // remote server allows CORS
          return true;
       }
     },
     waitSeconds: 5
  },
  baseUrl: siteUrl + 'static/lib/js',
  shim: {
    'underscore': { exports: '_'}
  },
  paths: {
    'upload': upload,
    'templates': templates,
    'progress': 'jquery.ajax-progress'
  }
});

define(['upload/upload'], function (upload) {

    $(function () {
        upload.initialize({
            form: '#file-uploader',
            dropZone: '#drop-zone',
            file_queue: '#file-queue',
            clear_button: '#clear-button',
            upload_button: '#upload-button'
        });
    });
});
