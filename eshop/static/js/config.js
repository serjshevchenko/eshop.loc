var require = {
            baseUrl: '/static/js',
            paths: {
                'jquery': 'vendor/jquery',
                'jqueryTE': 'vendor/jquery-te-1.4.0.min',
                'foundation': 'foundation/foundation',
                'foundationAccordion': 'foundation/foundation.accordion',
                //'foundationAbide': 'foundation/foundation.abide',
                //'foundationAlert': 'foundation/foundation.alert',
                //'foundationReveal': 'foundation/foundation.reveal',


                //pages
                'home': 'pages/home',
                'news': 'pages/news',
                'about': 'pages/about',
                'contact': 'pages/contact',
                'admin': 'pages/admin'
            },
            shim: {
                'foundation': {
                    deps: ['jquery']
                },
                'foundationAccordion': {
                    deps: ['foundation']
                },
                'jqueryTE': {
                    deps: ['jquery']
                }
            }
        };