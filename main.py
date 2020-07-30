from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)
  
# TODO: Get Flask app set up to create a login session