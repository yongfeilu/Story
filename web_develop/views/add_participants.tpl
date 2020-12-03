% include('header.tpl')
<!-- Main content should go here-->

<div class="row">
		<h1 style="text-align: center">Add Participants for {{film[0]}}</h1>
		% if err != None:
        <div class="container">
            <p style="color:red; text-align: center">{{err}}</p>
        </div>
        % end

		<div style="width: 25%; margin:25px auto;">
			<form name="myForm" action="/participants/{{movie_id}}" method="POST" enctype="multipart/form-data">
				
				<div class="form-group">
					<label for="prof_id" style="font-size: 18px">Professional ID</label>
					% if vals[0]:
						<input class="form-control" type = "number" name="prof_id" min="1", value="{{vals[0]}}">
					% else:
						<input class="form-control" type = "number" name="prof_id" min="1">
					% end
				</div>
				
				<div class="form-group">
					<label for="name" style="font-size: 18px">Name</label>
					% if vals[1]:
						<input class="form-control" type = "text" name="name" id="name" value="{{vals[1]}}">
					% else:
						<input class="form-control" type = "text" name="name" id="name">
					% end
				</div>

				<div class="form-group">
					<label for="gender" style="font-size: 18px">Gender</label>
					% if vals[2]:
						<select class="form-control" id="gender" name="gender">
							<option value="{{vals[2]}}">{{vals[2].title()}}</option>
						</select>
					% else:
						<select class="form-control" id="gender" name="gender">
							<option></option>
							<option value="female">Female</option>
							<option value="male">Male</option>
							<option value="other">Other</option>
						</select>
					% end
				</div>

				<div class="form-group">
					<label for="birthday" style="font-size: 18px">Date of Birth</label>
					% if vals[3]:
						<input class="form-control" type = "date" name="time" value="{{vals[3]}}">
					% else:
						<input class="form-control" type = "date" name="time">
					% end
				</div>

				<div class="form-group">
					<label for="country" style="font-size: 18px">Country</label>
					% if vals[4]:
						<input class="form-control" type="text" name="country" id="country" value="{{vals[4]}}">
					% else:
						<input class="form-control" type="text" name="country" id="country">
					% end		
				</div>

				<div class="form-group">
					<label for="occupation" style="font-size: 18px">Occupation</label>
					% if vals[5]:
						<input class="form-control" type = "text" name="occupation" id="occupation" value="{{vals[5]}}">
					% else:
						<input class="form-control" type = "text" name="occupation" id="occupation">
					% end
				</div>


				<div class="form-group">
					<button class="btn btn-lg btn-primary btn-block" name="add_new" value="add_new">Add A New Participant</button>
				</div>

				<hr>

				
				<div class="form-group">
					<label for="comment" style="font-size: 18px">Choose An Existing Person</label>

					<select class="form-control" name="ex_prof">
						<option></option>
						% for p in profs:
                        <option value="{{p[0]}}">{{p[0]}} -- {{p[1]}}</option>
                        % end
                    </select>
				</div>

				<div class="form-group">
					<button class="btn btn-lg btn-primary btn-block" name="add_exist" value="add_exist">Add An Existing Person</button>
				</div>
				
			</form>
			<a href="/movies" >Go Back</a>
		</div>
</div>




% include('footer.tpl')