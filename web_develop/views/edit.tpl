% include('header.tpl')
<!-- Main content should go here-->

<div class="row">
        <h1 style="text-align: center">Movie View/Edit</h1>
        % if err != None:
        <div class="container">
            <p style="color:red; text-align: center">{{err}}</p>
        </div>
        % end

        <div style="width: 25%; margin:25px auto;">

            <form action="/movies/{{data[0]}}" method="POST" enctype="multipart/form-data">
                
                <div class="form-group">
                    <label for="film">Film</label>
                    <input class="form-control" type = "text" name="name" value="{{data[1]}}" required>
                </div>

                <div class="form-group">
                    <label for="ID">ID</label>
                    <input class="form-control" type = "text" name="ID" value="{{data[0]}}" readonly>
                </div>


                <div class="form-group">
                    <label for="release_date"> Release Date</label>
                    <input class="form-control" type="date" name="release_date" value="{{data[2]}}" id="release_date" required>
                </div>

                <div class="form-group">
                    <label for="length">Length</label>
                    <input class="form-control" type="text" name="length" value="{{data[3]}}" required>
                </div>

                <div class="form-group">
                    <label for="language">Language</label>
                    <input class="form-control" type="text" name="language" value="{{data[4]}}" required>
                </div>

                <div class="form-group">
                    <label for="bugdet">Budget</label>
                    <input class="form-control" type="number" name="budget" value="{{data[5]}}" min="0" required>
                </div>

                <div class="form-group">
                    <label for="bugdet">Box Office</label>
                    <input class="form-control" type="number" name="box_office" value="{{data[6]}}" min="0" required>
                </div>

                <hr>
                <div class="form-group">
                    <button class="btn btn-lg btn-primary btn-block">Submit!</button>
                </div>
            </form>
            <a href="/movies">Go Back</a>
        </div>
</div>


% include('footer.tpl')