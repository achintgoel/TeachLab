/*global frontend, Backbone, JST*/

frontend.Views = frontend.Views || {};

(function () {
  frontend.Views.AppView = Backbone.View.extend({

    template: JST['app/scripts/templates/profile.hbs'],

    render: function(){
      this.$el.html(this.template());
      console.log('render');
      return this;
    }

  });

})();
