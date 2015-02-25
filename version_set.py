#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ktulhy'

import subprocess
import datetime


class Version:
    default = "0.0.0.0"

    def __init__(self):
        pass

    def parse(self, raw, version_format="{major}.{minor}.{build}.{revision}{release}"):

        # delete first 'v'
        raw = raw[1:] if 'v' == raw[0] else raw

        try:
            major_minor_release, build, revision = raw.split("-")
        except ValueError as e:
            print("Incorrect tag")
            print(e)
            return self.default

        try:
            major, minor_release = major_minor_release.split(".")
        except ValueError as e:
            print("Incorrect tag")
            print(e)
            return self.default

        i = 0
        while (len(minor_release) != i) and minor_release[i].isdigit():
            i += 1


        minor = minor_release[:i]
        release = minor_release[i:]
        try:
            version_ready = version_format.format(major=major,
                                                  minor=minor,
                                                  build=build,
                                                  revision=revision,
                                                  release="[%s]" % (release) if release else "")
        except KeyError as e:
            print("Incorrect version format")
            print(e)
            return self.default

        return version_ready

    def get_version(self):
        proc = subprocess.Popen("git describe --long --tags", shell=True, stdout=subprocess.PIPE)
        raw = proc.stdout.readline().rstrip().lstrip()
        if not raw:
            print("Something wrong with git")

        raw = raw.decode("utf-8")

        return self.parse(raw)

    def get_date(self):
        proc = subprocess.Popen("git show -s --format='%ct'", shell=True, stdout=subprocess.PIPE)
        date = proc.stdout.readline()

        date = datetime.datetime.fromtimestamp(
            int(date)
        ).strftime('%d.%m.%Y')
        return date

    def generate(self, lang, path):
        pass


version = Version()
print(version.get_version())
print(version.get_date())


# open("js/version.js", "wt").write("""var __version__ = "%s";
# var __date__ = "%s";""" %generate_version())
