## Development

### Install mamba

Download mamba-forge

### Manage pypi package

- https://pypi.org/project/mobie/

### Check versions on conda

- https://anaconda.org/conda-forge/mobie

### Create mobie-dev env

```
mamba create -y -n mobie-dev -c conda-forge openjdk=8 jgo pip maven blosc
```

### Test within Java on the command line

1. cd to the main folder of mobie-viewer-fiji
2. ./install.sh
3. ./mobie-files -r "/Users/tischer/Documents/mobie/src/test/resources/input/skimage-2d-tiff/" -i "image.tif" -l "segmentation.tif" -t "table.tsv" 

### Test within python using a local MoBIE build

1. mvn install current version (could be a SNAPSHOT)
2. hardcode this version in `__init__.py`: e.g., 
   `_artifactVersion         = '3.2.0-SNAPSHOT' #version("mobie")` 
   
continue as in [test locally](#test-locally)

### Release a new version

Example for version `3.0.10`:

#### mobie-viewer-fiji repo

Within the mobie Java code update the versions in all command line tools, e.g.:
```java
@CommandLine.Command(name = "mobie", mixinStandardHelpOptions = true, version = "3.0.10", description = "Visualise multi-modal big image data, see https://mobie.github.io/")
```

Use the below lines to make a maven release:

```
mamba activate mobie-dev # this activates java 8!
./install.sh  # test the line of code suggested by the script!
git add .; git commit -m "prepare for release"; git push
../scijava-scripts/release-version.sh --skip-version-check --skip-license-update
# if successful this will say
# * [new tag]mobie-viewer-fiji-3.0.10 -> mobie-viewer-fiji-3.0.10
```

#### mobie-cmd repo

Go to `setup.py` and change the `version` to `3.0.10`

```
git add setup.py
git commit -m "Version bump 3.0.10"
```


#### test locally

```
mamba activate mobie-dev
pip install -e .
mobie --help
mobie project -p "https://github.com/mobie/platybrowser-project"
mobie files -r "/Users/tischer/Documents/mobie/src/test/resources/input/skimage-2d-tiff/" -i "image.tif" -l "segmentation.tif" -t "table.tsv"
```

#### deploy to pypi

```
git tag 3.0.10
git push --tags
```

Pushing a tag triggers build and deploy to pypi via github actions that are configured in the mobie-cmd repo.

#### release on conda-forge

deploying to pypi (s.a.) automatically triggers a PR in https://github.com/conda-forge/mobie-feedstock


#### Troubleshooting

Remove a tag (remote and local):

```
git push origin --delete 3.0.10
git tag -d 3.0.10
```

