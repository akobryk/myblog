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








$(document).ready(function() {
	//setMarkdown();
	//highlightLang();
	contentImages();
	setPreviewContent(contentInput.val());
	setPreviewTitle(titleInput.val());

	
	
})

