# Azure DevOps pipelines for .NET binaries obfuscation

A build pipeline is scheduled to run every morning at 2AM UTC + a release pipeline scheduled at 3AM UTC to push the artifacts from the previous pipeline here - [Obfuscated](https://github.com/roxanakovaci/Azure-pipelines/releases/download/Obfuscated/Obfuscated.zip)

The build pipeline does the following:
1. git clones all the individual binaries from devs repos
2. runs each of them through InvisibilityCloak from https://github.com/h4wkst3r/InvisibilityCloak
3. random names are chosen for the new binaries from names.txt
4. keeps a record of all binaries names and their corresponding renames (in correlation.txt)
5. compiles and builds all the binaries
6. runs the compiled versions of each binary through ConfuserEx from https://github.com/mkaring/ConfuserEx

There is one caveat with InvisibilityCloak, it doesn't support repos with multiple projects in them so repos such as Farmer or InternalMonologue, etc have not been run through it but they're still obfuscated with ConfuserEx. Such repos will keep their original name.

## Credits
[mkaring](https://github.com/mkaring) for the awesome ConfuserEx project.

[h4wkst3r](https://github.com/h4wkst3r) for another awesome project - InvisibilityCloak
