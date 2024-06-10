def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    return ' '.join(word.title() for word in phrase.split())

# Test cases
print(titleize('this is awesome'))                   # Should print 'This Is Awesome'
print(titleize('oNLy cAPITALIZe fIRSt'))            # Should print 'Only Capitalize First'

