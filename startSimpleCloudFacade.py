# start from command line: python .\startSimpleCloudFacade.py -p 8080

import optparse
import ScfServer.server

def parseArguments():
    parser = optparse.OptionParser()
    parser.add_option("-p", "--port", dest="port", type="int", help="open server on PORT", metavar="PORT", default=80)

    (options, args) = parser.parse_args()
    return options

if __name__ == "__main__":
    options = parseArguments()
    ScfServer.server.serve(options.port)