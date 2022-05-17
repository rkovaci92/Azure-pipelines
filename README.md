# Azure DevOps pipelines for post-exploitation .NET binaries obfuscation


A build pipeline is scheduled to run every morning at 2AM UTC + a release pipeline scheduled at 3AM UTC to push the artifacts from the previous pipeline here - https://github.com/roxanakovaci/Azure-pipelines/releases/download/Obfuscated/Obfuscated.zip 

The build pipeline does the following:
1. git clones all the individual binaries from devs repos;
2. runs each of them through InvisibilityClocks from https://github.com/h4wkst3r/InvisibilityCloak
3. keeps a record of all binaries names and their corresponding renames (in correlation.txt)
5. compiles and builds all the binaries
6. runs the compiled versions of each binary through ConfuserEx from https://github.com/mkaring/ConfuserEx
