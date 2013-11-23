/*global frontend, Backbone, JST*/

frontend.Views = frontend.Views || {};

(function () {
    'use strict';

    frontend.Views.AppView = Backbone.View.extend({

        template: JST['app/scripts/templates/app.hbs']

    });

})();
