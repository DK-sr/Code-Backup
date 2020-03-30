# Code Backup Script

* **option.yaml**: change repo url as yours.

### Dependency
* PyYAML : pip install PyYAML



## How To Use It

Add crontab job.

```shell
$ sudo crontab -e
1 2 3 4 5 ./run.sh
```



* 1: Minutes(0~59)
* 2: Hours(0~23)
* 3: Days(1~31)
* 4: Month(1-12)
* 5: Day of the week(1-7)

```shell
#EX)
0 2 * * * ./run.sh
```

