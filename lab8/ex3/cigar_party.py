def cigar_party(cigars, is_weekend):
    if (cigars >= 40 and cigars <= 60) and not is_weekend:
        return True
    if (cigars >= 40 and cigars <= 60) and is_weekend:
        return True
    if (cigars > 60) and is_weekend:
        return True

    if (cigars < 40 or cigars > 60) and is_weekend:
        return False
    return False