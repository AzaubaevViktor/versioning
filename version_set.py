#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ktulhy'

import subprocess
import datetime
import sys
import _version


class Version:
    default = "0.0.0.0"
    languages = {
        "java":
            """package {package};

public class Version {{
    public String version = "{version}";
    public String date = "{date}";
}}
""",
        "python":
        """# -*- coding:utf-8 -*-
version = "{version}"
date = "{date}" """
    }

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
        if "java" == lang:
            package = ".".join(path.split('/')[:-1])
            data = self.languages[lang].format(package=package,
                                               version=self.get_version(),
                                               date=self.get_date())
            open(path, mode='w').write(data)
        elif "python" == lang:
            data = self.languages[lang].format(version=self.get_version(),
                                               date=self.get_date())
            open(path, mode='w').write(data)
        pass

print("Versioning v{version} by {date}".format(version=_version.version,
                                               date=_version.date))

version = Version()
print(version.get_version())
print(version.get_date())

argc = len(sys.argv)

if 3 != argc:
    print("Use `versioning %lang% %path%`")
    exit(1)

lang = sys.argv[1]
path = sys.argv[2]

version.generate(lang, path)