from CJsonNLTK import CJsonNLTK
import argparse


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument("target", help="word in here", type=str)
    parse.add_argument("-s", help="save to json", required=False, default=False)
    parse.add_argument("-p", help="print to json", required=False, default=True)

    args = parse.parse_args()

    if args.s:
        jnltk = CJsonNLTK(args.target)
        jnltk.setDefinition()
        jnltk.setSynonymsAntonyms()
        jnltk.save2Json(args.s)
        exit(1)

    if args.p:
        jnltk = CJsonNLTK(args.target)
        jnltk.setDefinition()
        jnltk.setSynonymsAntonyms()
        jnltk.pprint2Json()
        exit(1)

