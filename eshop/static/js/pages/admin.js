define(['jquery', 'jqueryTE', 'foundationAccordion'], function() {
    //$('#about-page-content').jqte();
    var foundation_options = {
        accordion: {
            multi_expand: true
        }
    };
    $(document).foundation(foundation_options);
    return {};
});
