#!/usr/bin/env python3
# -*- coding: utf-8 -*

import click

@click.command(help='aws region list command')
def cmd():
    region =  'us-east-1        米国東部（バージニア北部）\n' \
              'us-east-2        米国東部 (オハイオ) \n' \
              'us-west-1        米国西部 (北カリフォルニア) \n' \
              'us-west-2        米国西部 (オレゴン) \n' \
              'ca-central-1     カナダ (中部) \n' \
              'eu-west-1        欧州 (アイルランド) \n' \
              'eu-central-1     欧州 (フランクフルト) \n' \
              'eu-west-2        欧州 (ロンドン) \n' \
              'ap-northeast-1   アジアパシフィック (東京) \n' \
              'ap-northeast-2   アジアパシフィック (ソウル) \n' \
              'ap-southeast-1   アジアパシフィック (シンガポール) \n' \
              'ap-southeast-2   アジアパシフィック (シドニー) \n' \
              'ap-south-1       アジアパシフィック (ムンバイ) \n' \
              'sa-east-1        南米 (サンパウロ)'

    click.echo(region)


def main():
    cmd()


if __name__ == '__main__':
    main()
