def sample_function(**demographic):
    for keys, values in demographic.items():
        print(f"My  {values} is for {keys}")


sample_function(age=34, name="Sarah", address="123 Main Street")