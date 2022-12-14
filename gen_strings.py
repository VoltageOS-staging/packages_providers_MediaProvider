#!/usr/bin/env python
#
# Copyright (C) 2019 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Helper script to generate tedious strings.xml permutations
"""

from string import Template

verbs = ["write","trash","untrash","delete"]
datas = [("audio","audio file"),("video","video"),("image","photo"),("generic","item")]

print '''
<!-- ========================= BEGIN AUTO-GENERATED BY gen_strings.py ========================= -->'''

for verb in verbs:
    verblabel = verb
    if verb == "write":
        verblabel = "modify"

    print '''
<!-- ========================= %s STRINGS ========================= -->
''' % (verb.upper())
    for data, datalabel in datas:
        if verb == "trash":
            print Template('''
<!-- Dialog title asking if user will allow $verb permission to the $data item displayed below this string. [CHAR LIMIT=128] -->
<string name="permission_${verb}_${data}"> {count, plural,
    =1    {Allow <xliff:g id="app_name" example="Gmail">^1</xliff:g> to move this $datalabel to trash?}
    other {Allow <xliff:g id="app_name" example="Gmail">^1</xliff:g> to move <xliff:g id="count" example="42">^2</xliff:g> ${datalabel}s to trash?}
}</string>
''').substitute(vars()).strip("\n")
            print Template('''
<!-- Progress dialog message after user allows $verb permission to the $data item [CHAR LIMIT=128] -->
<string name="permission_progress_${verb}_${data}"> {count, plural,
    =1    {Moving $datalabel to trash&#8230;}
    other {Moving <xliff:g id="count" example="42">^1</xliff:g> ${datalabel}s to trash&#8230;}
}</string>
''').substitute(vars()).strip("\n")

        elif verb == "untrash":
            print Template('''
<!-- Dialog title asking if user will allow $verb permission to the $data item displayed below this string. [CHAR LIMIT=128] -->
<string name="permission_${verb}_${data}"> {count, plural,
    =1    {Allow <xliff:g id="app_name" example="Gmail">^1</xliff:g> to move this $datalabel out of trash?}
    other {Allow <xliff:g id="app_name" example="Gmail">^1</xliff:g> to move <xliff:g id="count" example="42">^2</xliff:g> ${datalabel}s out of trash?}
}</string>
''').substitute(vars()).strip("\n")
            print Template('''
<!-- Progress dialog message after user allows $verb permission to the $data item [CHAR LIMIT=128] -->
<string name="permission_progress_${verb}_${data}"> {count, plural,
    =1    {Moving $datalabel out of trash&#8230;}
    other {Moving <xliff:g id="count" example="42">^1</xliff:g> ${datalabel}s out of trash&#8230;}
}</string>
''').substitute(vars()).strip("\n")

        else:
            print Template('''
<!-- Dialog title asking if user will allow $verb permission to the $data item displayed below this string. [CHAR LIMIT=128] -->
<string name="permission_${verb}_${data}"> {count, plural,
    =1    {Allow <xliff:g id="app_name" example="Gmail">^1</xliff:g> to $verblabel this $datalabel?}
    other {Allow <xliff:g id="app_name" example="Gmail">^1</xliff:g> to $verblabel <xliff:g id="count" example="42">^2</xliff:g> ${datalabel}s?}
}</string>
''').substitute(vars()).strip("\n")
            if verb == "write":
                actionLabel = "Modifying"
            else:
                actionLabel = "Deleting"
            print Template('''
<!-- Progress dialog message after user allows $verb permission to the $data item [CHAR LIMIT=128] -->
<string name="permission_progress_${verb}_${data}"> {count, plural,
    =1    {$actionLabel $datalabel&#8230;}
    other {$actionLabel <xliff:g id="count" example="42">^1</xliff:g> ${datalabel}s&#8230;}
}</string>
''').substitute(vars()).strip("\n")

print '''
<!-- ========================= END AUTO-GENERATED BY gen_strings.py ========================= -->
'''
