import wikipedia


def Search(subject):

	wikipedia.page(subject)

	Title			= 	(wikipedia.page(subject).title)
	Url 			=	(wikipedia.page(subject).url)
	Content			=	(wikipedia.page(subject).content)
	References		=	(wikipedia.page(subject).references)
	Related_links		=	(wikipedia.page(subject).links)

	return Title, Url, Content, References, Related_links




