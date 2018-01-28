import React from 'react';
import Dropzone from 'react-dropzone';
import request from 'superagent';


class UploadForm extends React.Component {
    constructor() {
        super();
        this.state = { files: [] }
    }

    onDrop(files) {
        this.setState({
            files
        });

        let req = request.post('/image');
        req.attach('file', files[0]);
        req.end((err, res) => {
            console.log(err);
            console.log(res);
        });
    }

    render() {
        return (
            <section>
                <div className="dropzone">
                    <Dropzone onDrop={this.onDrop.bind(this)}>
                        <p>Try dropping some files here, or click to select files to upload.</p>
                    </Dropzone>
                </div>
                <aside>
                    <h2>Dropped files</h2>
                    <ul>
                        {
                            this.state.files.map(f => <li key={f.name}>{f.name} - {f.size} bytes</li>)
                        }
                    </ul>
                </aside>
            </section>
        );
    }
}

export default UploadForm;
