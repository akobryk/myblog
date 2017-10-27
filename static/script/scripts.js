// Infinite Scroll
//...............................................................................

/*var infinite = new Waypoint.Infinite({
		element: $('.infinite-container')[0],
		onBeforePageLoad:function() {
			$('.loading').show();
		},
		onAfterPageLoad: function ($items) {
			$('.loading').hide();
		}
	});*/

// Go To Top Button 
//...............................................................................

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() { scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("myBtnToTop").style.display = "block";
    } else {
        document.getElementById("myBtnToTop").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Chrome, Safari and Opera
    document.documentElement.scrollTop = 0; // For IE and Firefox
} 

// Datetimepicker
//...............................................................................
function initDateFields() {

	// a publish field
	var calendar = $('input#id_publish');
	$('#div_id_publish div').addClass('input-group');
	$('<span class="input-group-btn"><button class="btn btn-info" type="button">\
		<span class="fa fa-calendar"></span></button></span>').insertAfter(calendar);
	// a birhday date field
	var birthday = ('input#id_birthday');
	$('#div_id_birthday div').addClass('input-group');
	$('<span class="input-group-btn"><button class="btn btn-info" type="button">\
		<span class="fa fa-calendar"></span></button></span>').insertAfter(birthday);
	$(calendar).datetimepicker({
		'format': 'YYYY-MM-DD'
	});

	$(birthday).datetimepicker({
		'format': 'YYYY-MM-DD'
	});
}

// About page
//...............................................................................
function initAbout() {
	$('li a#about-page').click(function(event) {
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'success': function(data, status, xhr) {
				if (status != 'success') {
					alert('error');
					return false;
				}
				var modal = $('#myLargeModal')
				var html = $(data)
				var content = html.find('.col-about p')
				modal.find('.modal-title').html(html.find('.col-about h3').text());
				modal.find('.modal-body').html(content);
				initAboutForm(content, modal);
				modal.modal('show')
			},
			'error': function() {
				alert('error');
				return false;
			}
		});
		return false;
	});
}

function initAboutForm(content, modal) {
	content.ajaxForm({
		'dataType': 'html',
		'error': function() {
			alert('error(form)');
			return false;
		},
		'success': function(data, status, xhr) {
			var html = $(data)
			var newcontent = html.find('#col-about p');
			modal.find('.modal-body').html(html.find('.alert'));

			if (newform.length > 0 ) {
				modal.find('.modal-body').append(newform);

				initAboutForm(newcontent, modal);
			} 

		}
	});
}



// Contact Admin Modal
//...............................................................................
function initContactAdmin() {
	$('li a#contact-admin-modal').click(function(event) {
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'success': function(data, status, xhr) {
				if (status != 'success') {
					alert('error');
					return false;

				}
				var modal = $('#myModal')
				var html = $(data)
				var form = html.find('#content-col form');
				modal.find('.modal-title').html(html.find('#content-col h3').text());
				modal.find('.modal-body').html(form);

				initContactAdminForm(form, modal);
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true
				});
			},
			'error': function() {
				alert('error');
				return false;
			}
		});
		return false;
	});
}

function initContactAdminForm(form, modal) {

	refreshCaptcha();
	form.ajaxForm({
		'dataType': 'html',
		'error': function() {
			alert('error(form)');
			return false;
		},
		'success': function(data, status, xhr) {
			var html = $(data)
			var newform = html.find('#contect-col form');
			modal.find('.modal-body').html(html.find('.alert'));

			if (newform.length > 0 ) {
				modal.find('.modal-body').append(newform);

				initContactAdminForm(newform, modal);
			} else {
				setTimeout(function(){location.reload(true);}, 3000);
			}

		}
	});
}

// Markdown 
//...............................................................................

function setMarkdown() {
	$('.content-markdown').each(function(){
		var content = $(this).text()
		//content.trim()
		var markedContent = marked(content)
		});
		$(this).html(markedContent)

	}

// Highlight program lang 
//...............................................................................
/*
function highlightLang() {
		hljs.initHighlightingOnLoad();
	}
	
}
*/
function contentImages() {
	$('.content-item img').each(function() {
		$(this).addClass('img-fluid')

	});

}


var titleInput = $('#id_title');
function setPreviewTitle(value) {
	$('#preview-title').text(value)
	
}

var contentInput = $('#id_content');
function setPreviewContent(value){
	var markedContent = marked(value)
	$('#preview-content').html(markedContent)
	$('#preview-content img').each(function(){
		$(this).addClass('img-fluid')
	});

}

titleInput.keyup(function(){
		var newContent = $(this).val()
		setPreviewTitle(newContent)
	});

contentInput.keyup(function(){
		var newContent = $(this).val()
		setPreviewContent(newContent)
	});



// Spinner 
//..........................................................................

function initSpinner(){
	$('#button-spinner').click(function() {
       $('#spinner').show()
    });

    $('#button-spinner1').click(function() {
       $('#spinner').show();
    });
    $('#button-spinner2').click(function() {
       $('#spinner').show();
    });
     $('#button-spinner3').click(function() {
       $('#spinner').show();
    });
     $('#button-spinner4').click(function() {
       $('#spinner').show();
    });
     $('#button-sp-detail').click(function() {
       $('#spinner').show();
    });
      $('#button-sp-detail_1').click(function() {
       $('#spinner').show();
    });

     
}


function initCloseAlertMessage() {
	$('#close-alert-btn').click(function(event) {
		$('#alert-message').hide()
	})
}

function refreshCaptcha() {
    // Add refresh button after field (this can be done in the template as well)
    $('img.captcha').wrap(
            $('<a href="#void" class="captcha-refresh" title="Refresh"></a>')
            );

    // Click-handler for the refresh-link
    $('.captcha-refresh').click(function(){
        var $form = $(this).parents('form');
        var url = location.protocol + "//" + window.location.hostname + ":"
                  + location.port + "/captcha/refresh/";

        // Make the AJAX-call
        $.getJSON(url, {}, function(json) {
            $form.find('input[name="captcha_0"]').val(json.key);
            $form.find('img.captcha').attr('src', json.image_url);
        });

        return false;
    });
};

$(document).ready(function() {
	//setMarkdown();
	//highlightLang();
	initSpinner();
	initCloseAlertMessage();
	refreshCaptcha();
	initDateFields();
	contentImages();
	initContactAdmin();
	initAbout();
	setPreviewContent(contentInput.val());
	setPreviewTitle(titleInput.val());
	

	
	
})

