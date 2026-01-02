def count_log_level(logs):


    count = {}

    for log in logs:
        level = log.split(":")[0].upper()

        if level in count:
            count[level] += 1

        else:
            count[level]=1

    return count



logs=["INFO: User logged in", "ERROR: Connection failed", "INFO: Upload complete"]
print(count_log_level(logs))