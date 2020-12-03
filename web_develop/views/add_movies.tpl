% include('header.tpl')
<!-- Main content should go here-->


<div class="row">
        <h1 style="text-align: center">Add a New Movie</h1>
        % if err != None:
        <div class="container">
            <p style="color:red; text-align: center">{{err}}</p>
        </div>
        % end

        <div style="width: 25%; margin:25px auto;">

            <form action="/movies" method="POST" enctype="multipart/form-data">


                <div class="form-group">
                    <label for="film">Film</label>
                    % if vals[0]:
                        <input class="form-control" type = "text" name="title" value="{{vals[0]}}" required>
                    % else:
                        <input class="form-control" type = "text" name="title" required>
                    % end
                    
                </div>

                <div class="form-group">
                    <label for="release_date"> Release Date</label>
                    % if vals[0]:
                        <input class="form-control" type="date" name="release_date" id="release_date" value="{{vals[1]}}" required>
                    % else:
                        <input class="form-control" type="date" name="release_date" id="release_date" required>
                    % end
                    
                </div>

                <div class="form-group">
                    <label for="length">Length</label>
                    % if vals[0]:
                        <input class="form-control" type="text" name="length" value="{{vals[2]}}" required>
                    % else:
                        <input class="form-control" type="text" name="length" placeholder="xx:xx:xx" required>
                    % end
                    
                </div>

                <div class="form-group">
                    <label for="language">Language</label>
                    % if vals[0]:
                        <input class="form-control" type="text" name="language" value="{{vals[3]}}" required>
                    % else:
                        <input class="form-control" type="text" name="language" required>
                    % end
                    
                </div>

                <div class="form-group">
                    <label for="bugdet">Budget</label>
                    % if vals[0]:
                        <input class="form-control" type="number" name="budget" value="{{vals[4]}}" min="0" required>
                    % else:
                        <input class="form-control" type="number" name="budget" min="0" required>
                    % end
                    
                </div>

                <div class="form-group">
                    <label for="bugdet">Box Office</label>
                    % if vals[0]:
                        <input class="form-control" type="number" name="box_office" value="{{vals[5]}}" min="0" required>
                    % else:
                        <input class="form-control" type="number" name="box_office" min="0" required>
                    % end
                    
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