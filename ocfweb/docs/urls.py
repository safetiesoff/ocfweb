import re
from itertools import chain

from django.conf.urls import url
from django.http import Http404

from ocfweb.docs.doc import Document
from ocfweb.docs.markdown_based import get_markdown_docs
from ocfweb.docs.views.hosting_badges import hosting_badges
from ocfweb.docs.views.index import docs_index
from ocfweb.docs.views.servers import servers


DOCS = {
    doc.name: doc
    for doc in chain(
        [
            Document(name='/staff/backend/servers', title='Servers', render=servers),
            Document(name='/services/vhost/badges', title='Hosting badges', render=hosting_badges),
        ],
        get_markdown_docs(),
    )
}


def render_doc(request, doc_name):
    """Render a document given a request."""
    doc = DOCS['/' + doc_name]
    if not doc:
        raise Http404()
    return doc.render(doc, request)


def doc_name(doc_name):
    # we can't actually deal with escaping into a regex, so we just use a whitelist
    assert re.match('^/[a-zA-Z\-/]+$', doc_name), 'Bad document name: ' + doc_name
    return doc_name[1:].replace('-', '\-')

doc_names = '|'.join(map(doc_name, DOCS.keys()))


urlpatterns = [
    url('^/$', docs_index, name='docs'),

    # we use a complicated generated regex here so that we have actual
    # validation of URLs (in other words, if you try to make a link to a
    # missing document, it will fail)
    url('^/({doc_names})/$'.format(doc_names=doc_names), render_doc, name='doc'),
]
