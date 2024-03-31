from scheduler_tasks import create_rep, request, file
from scheduler_data.URL import url
from scheduler import Scheduler
from job import Job


def main():
    scheduler = Scheduler()
    job = Job()
    dir_gen = create_rep("test_folder")
    request_gen = request(url)
    file_gen = file(next(request_gen))

    for value in dir_gen:
        pass

    for value in request_gen:
        pass

    for value in file_gen:
        pass


if __name__ == "__main__":
    main()
