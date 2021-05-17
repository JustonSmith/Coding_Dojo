// You should be familiar with routing at this point. When you go to https://www.codingdojo.com, you are visiting a website. If you then visit https://www.codingdojo.com/web-development-courses, you are going to another route. This follows the request/response cycle, where you make a request to the server, and it sends HTML, CSS, and Javascript back to you dynamically depending on what route you are visiting.

// However, in a Single Page Application, routing does not make sense in the same way. We know that when you first visit a site, all the HTML, CSS and Javascript are all loaded. So, how would routing even work? It seems like it would be inefficient to reload everything with a new route, and it defeats the purpose of a Single Page Application, right?

// Well, we need to change our understanding of routing when dealing with SPAs. In SPAs, we will use routing, but only in a very superficial sense. We will go to a new route, but we will actually not necessarily be making another request to the server. Instead, this pseudo-route will just tell our SPA which part of the page we want to see. So, if you are not making requests to an API, visiting a new route in an SPA is not actually making another request. It is just a way to tell our SPA the portion of the app we want to see. This gives the illusion to the user that they are visiting another route.

// Let's consider a dynamic site setup. If you are on a website like Facebook, and it is using an SPA, going to a new page changes the UI (HTML, CSS and Javascript), but there is also data that is loaded. We know that if we refresh a page, and there has been a new Facebook post, that post will show up after refresh. That clues us in that the data is not sent in with the first response. This is because when we go to a new "pseudo-route" in which it grabs data from our database, we actually are going to make an asynchronous request (AJAX) to our server to grab the data, and just update the DOM with that data. Other than that, the HTML, CSS and Javascript will just be loaded based on what was sent in the first request.

