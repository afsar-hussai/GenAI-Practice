class OurOwnError(Exception):
    pass

def chai_count(metric):
    if metric<0:
        raise OurOwnError("Metric can't be negative")
    print(f"count is {metric}")


chai_count(-4)