echo -e "machine github.com\n  login $GITHUB_TOKEN" >~/.netrc
git config --local user.name "Travis CI"
git config --local user.email "travis@noreply.github.com"
git checkout -b travis
git add Configs/*.json
git commit -m "Auto JSON code format [ci skip]"
git push origin travis:master
