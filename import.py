
from testrail import TestRail
from argparse import ArgumentParser

def main(args):

    tr_source = TestRail(
        project_id=args.source_proj,
        email=args.source_user,
        key=args.source_pass,
        url=args.source_url
    )

    tr_target = TestRail(
        project_id=args.target_proj,
        email=args.target_user,
        key=args.target_pass,
        url=args.target_url
    )

    return

if __name__ == '__main__':

    parser = ArgumentParser()

    parser.add_argument('--source_proj', dest='source_proj', action='store')
    parser.add_argument('--source_user', dest='source_user', action='store')
    parser.add_argument('--source_pass', dest='source_pass', action='store')
    parser.add_argument('--source_url', dest='source_url', action='store')

    parser.add_argument('--target_proj', dest='target_proj', action='store')
    parser.add_argument('--target_user', dest='target_user', action='store')
    parser.add_argument('--target_pass', dest='target_pass', action='store')
    parser.add_argument('--target_url', dest='target_url', action='store')

    args = parser.parse_args()
    main(args)
