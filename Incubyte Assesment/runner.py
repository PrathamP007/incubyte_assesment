from behave.__main__ import main as behave_main

if __name__ == "__main__":
    behave_main([
        "features",
        "--no-capture",           # print all exceptions
        "--no-capture-stderr",    # print stderr
        "-f", "pretty",
        "--tags=@smoke"
    ])
