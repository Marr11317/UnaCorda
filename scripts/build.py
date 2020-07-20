import fontforge

def generateWithFeatures(font, fea, name, dest="./redist/"):
    # make sure no old lookups remain
    for l in font.gpos_lookups:
        font.removeLookup(l)
    for l in font.gsub_lookups:
        font.removeLookup(l)
    font.mergeFeature(fea)
    font.familyname = name
    font.fontname = name
    font.appendSFNTName("English (US)", "Family", name)
    font.appendSFNTName("English (US)", "Fullname", name)
    font.generate(dest + name + ".otf")
    font.generate(dest + name + ".ttf")


if __name__ == "__main__":

    print("Opening UnaCorda.sfd")
    f = fontforge.open("./src/fonts/UnaCorda.sfd")
    print("generating UnaCorda.otf")
    generateWithFeatures(f, "./src/Features.fea", "UnaCorda")
    print("Closing UnaCorda.sfd")
    f.close()

    print("Opening WalkingBossa.sfd")
    f = fontforge.open("./src/fonts/WalkingBossa.sfd")
    print("generating WalkingBossa.otf")
    generateWithFeatures(f, "./src/Features.fea", "WalkingBossa")
    print("Closing WalkingBossa.sfd")
    f.close()
