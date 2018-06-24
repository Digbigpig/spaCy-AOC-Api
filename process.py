import spacy


def asc_parser(docx):
    """Returns a list of dictionaries containing the verb, object, and context of each sentence given.
    """

    nlp = spacy.load('en')
    doc = nlp(docx)
    return_list = []

    for sent in doc.sents:

        parsed = {'action': '', 'object': '', 'context': ''}
        for word in sent:

            if word.dep_ == 'dobj':

                span = ''
                for child in word.lefts:
                    if span:
                        span += ' '
                    span += child.text

                span += (' ' + word.text)

                for sub in word.children:
                    if sub.dep_ == 'conj':
                        span += ' '
                        for child in sub.subtree:

                            span += (child.text + ' ')

                parsed['object'] = str(span)
                parsed['action'] = str(word.head)

            if word.dep_ == 'pobj':
                for child in word.lefts:
                    parsed['context'] += str(child.text) + ' '
                parsed['context'] += str(word.text) + ' '
                for child in word.rights:
                    parsed['context'] += str(child.text) + ' '

        print("Action: ", parsed['action'])
        print("Object: ", parsed['object'])
        print('Context: ', parsed['context'])
        print('{}\n'.format(parsed))
        return_list.append(parsed)
    print("Return List ===> {}".format(return_list))
    return return_list









