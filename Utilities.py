class Utilities:

    @staticmethod
    def removeEscapeData(scrapedString):

        scrapedString = scrapedString.replace('\t', '')
        scrapedString = scrapedString.replace('\n', '')
        return scrapedString
