import collections
import string

TRANSLATION_TABLE = string.maketrans("", "")
SYNONYM_TO_CANONICAL = {
    'after the funeral': 'funerals are fatal',
    'death in the clouds': 'death in the air',
    'dumb witness': 'poirot loses a client',
    'five little pigs': 'murder in retrospect',
    'hercule poirots christmas': 'murder for christmas',
    'a holiday for murder': 'murder for christmas',
    'hickory dickory dock': 'hickory dickory death',
    'lord edgware dies': 'thirteen at dinner',
    'mrs mcgintys dead': 'blood will tell',
    'murder in the mews': 'dead mans mirror',
    'murder on the orient express': 'murder in the calais coach',
    'one two buckle my shoe': 'overdose of death',
    'the patriotic murders': 'overdose of death',
    'taken at the flood': 'there is a tide',
    'the hollow': 'murder after hours',
    'three act tragedy': 'murder in three acts'
}

ALL_BOOKS = [
    "After the Funeral",
    "Appointment with Death",
    "Black Coffee",
    "Cards on the Table",
    "Cat Among the Pigeons",
    "Curtain",
    "Dead Man's Folly",
    "Death in the Clouds",
    "Death on the Nile",
    "Double Sin and Other Stories",
    "Dumb Witness",
    "Elephants Can Remember",
    "Evil Under the Sun",
    "Five Little Pigs",
    "Hallowe'en Party",
    "Hercule Poirot's Christmas",
    "Hickory Dickory Dock",
    "Lord Edgware Dies",
    "Mrs McGinty's Dead",
    "Murder in Mesopotamia",
    "Murder in the Mews",
    "Murder on the Orient Express",
    "One, Two, Buckle My Shoe",
    "Peril at End House",
    "Poirot Investigates",
    "Poirot's Early Cases",
    "Problem at Pollensa Bay and Other Stories",
    "Sad Cypress",
    "Taken at the Flood",
    "The A.B.C. Murders",
    "The Adventure of the Christmas Pudding",
    "The Big Four",
    "The Clocks",
    "The Harlequin Tea Set",
    "The Hollow",
    "The Labours of Hercules",
    "The Murder of Roger Ackroyd",
    "The Murder on the Links",
    "The Mysterious Affair at Styles",
    "The Mystery of the Blue Train",
    "The Regatta Mystery and Other Stories",
    "The Under Dog and Other Stories",
    "Third Girl",
    "Three Act Tragedy",
    "While the Light Lasts and Other Stories"]

BOOKS_I_HAVE = [
    "A holiday for murder",
    "The hollow",
    "Cat among the pigeons",
    "Death on the Nile",
    "Elephants can remember",
    "The murder of Roger Ackroyd",
    "Halloween party",
    "Murder in Mesopotamia",
    "Funerals are fatal",
    "Evil under the sun",
    "The under dog and other stories",
    "Peril at end house",
    "Appointment with death",
    "Mrs. McGinty's dead",
    "Hickory dickory death",
    "The mystery of the blue train",
    "Thirteen at dinner",
    "Dead man's mirror",
    "Cards on the table",
    "Murder in retrospect",
    "And then there none",
    "The labours of Hercules",
    "Murder in three acts",
    "Dead man's folly",
    "The Mysterious Affair at Styles"]

def Sanitize(s):
    s = s.lower()
    s = s.translate(TRANSLATION_TABLE, string.punctuation)
    return s

def Canonicalize(s):
    if s in SYNONYM_TO_CANONICAL:
        return SYNONYM_TO_CANONICAL[s]
    else:
        return s

def FindBooksIDontHave(all_books, books_i_have):
    all_books = set(Canonicalize(Sanitize(b)) for b in all_books)
    books_i_have = set(Canonicalize(Sanitize(b)) for b in books_i_have)
    not_have = all_books - books_i_have
    dont_exist = books_i_have - all_books

    canonical_to_synonyms = collections.defaultdict(list)
    for s,c in SYNONYM_TO_CANONICAL.iteritems():
        canonical_to_synonyms[c].append(s)

    print 'There are %s books I don\'t have:' % len(not_have)
    for b in sorted(not_have):
        synonyms = canonical_to_synonyms[b]
        if synonyms:
            print '\t%s (also published as: %s)' % (b, ' and '.join(synonyms))
        else:
            print '\t%s' % b

    if dont_exist:
        print 'Books I have but don\'t exist:\n%s' % '\n'.join(sorted(dont_exist))

FindBooksIDontHave(ALL_BOOKS, BOOKS_I_HAVE)
