function prepareDocument() {
    jQuery('#carousel_example_generic').carousel({interval : false});
					jQuery("#carousel_right").click(function (e) {
						e.preventDefault();
						jQuery('#carousel_example_generic').carousel('next');
					});
					jQuery("#carousel_left").click(function (e) {
						e.preventDefault();
						jQuery('#carousel_example_generic').carousel('prev');
					});

	 $('.course-document').annotator()
}
jQuery(document).ready(prepareDocument);