import click
import sqlite3


conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        try:
            cmd_name = ALIASES[cmd_name].name
        except KeyError:
            pass
        return super().get_command(ctx, cmd_name)

@click.command(cls=AliasedGroup)
def cli():
    print("Tasks 0.1")
    print("-------------------\n")

@click.command()
@click.argument('task_text')
@click.argument('end_date')
def add(task_text, end_date):
    params = (task_text, end_date)
    cursor.execute("INSERT INTO tasks VALUES(NULL, ?, ?)", params)
    conn.commit()
    print("Added task: " + task_text + " with " + end_date + " end date")
    conn.close()

@click.command()
@click.option('--i', type=int)
def showall(i):
    if i == True:
        cursor.execute("SELECT * FROM tasks WHERE id = " + str(i))
        print(cursor.fetchall())
    else:
        for row in cursor.execute("SELECT * FROM tasks ORDER BY id"):
            print(row)
    conn.close()


@click.command()
@click.argument('i')
def remove(i):
    params = (i)
    cursor.execute("DELETE FROM tasks WHERE id = ?", params)
    conn.commit()
    print("Task with id " + i + " deleted")
    conn.close()
    

cli.add_command(add)
cli.add_command(showall)
cli.add_command(remove)

ALIASES = {
    "a": add,
    "show": showall,
    "del": remove
    }

if __name__ == "__main__":
    cli()
