from flask import Flask, render_template, request, redirect, url_for
app=Flask()

@app.route("/")
def home(user):
    return f"Welcome to  {user} with Ashish AI hub"