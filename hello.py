import wikipedia


def Search(s):

	wikipedia.page(s)

	Title			= 	(wikipedia.page(s).title)
	Url 			=	(wikipedia.page(s).url)
	Content			=	(wikipedia.page(s).content)
	References		=	(wikipedia.page(s).references)
	Related_links		=	(wikipedia.page(s).links)

	return Title, Url, Content, References, Related_links




