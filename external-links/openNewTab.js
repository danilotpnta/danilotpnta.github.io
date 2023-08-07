(function() {
  for (const link of document.getElementsByTagName('a')) {
    if (/^(https?:)?\/\//.test(link.getAttribute('href'))) link.target = '_blank';
  }
})();



//button.addEventListener('click', () => {
//    // open an empty window
//    const tab = window.open('about:blank')
//
//    // make an API call
//    fetch('https://reqres.in/api/users')
//      .then(res => res.json())
//      .then(json => {
//        // TODO: do something with JSON response
//
//        // update the actual URL
//        tab.location = 'https://github.com/danilotpnta?tab=repositories/'
//        tab.focus()
//      })
//      .catch(err => {
//        // close the empty window
//        tab.close()
//      })
//})
//
//
//printButtonClicked: function(){
//	var id = (new Date()).getTime();
//	var myWindow = window.open(window.location.href);
//	$.post("/ajax/friendlyPrintPage", postData).done(function(htmlContent) {
//		myWindow.document.write(htmlContent);
//		myWindow.focus();
//	});
//}