import os
import click

chunk_location = "./output"

def create_chunks(infile):
    filecount = 0
    chunksize = 1048576
    with open(os.path.abspath(infile), 'rb') as vid_f:
        while True:
            chunk = vid_f.read(chunksize)
            if not chunk:
                break
            with open(os.path.join(chunk_location, str(filecount)), 'wb') as out_f:
                out_f.write(chunk)
            filecount += 1

def reassemble_chunks(outfile):
    with open(os.path.abspath(str(outfile)), 'wb') as out_f:
        for filenum in range(0, len([f for f in os.listdir(chunk_location) if os.path.isfile(os.path.join(chunk_location, f))])-1):
            with open(os.path.join(chunk_location, str(filenum)), 'rb') as in_f:
                out_f.write(in_f.read())

def veirfy(infile, outfile):
    # TODO: Write this function so that we can check that the file was reassembled properly
    # Planned Checks:
    # 1. Hash of first X bytes
    # 2. File size
    # 3. Byte-by-byte comparison
    pass

@click.command()
@click.option('-i', '--input_file')
@click.option('-o', '--output_file')
@click.option('-c', '--chunk', is_flag=True)
@click.option('-a', '--assemble', is_flag=True)
@click.option('-v', '--verify')
def main(input_file, output_file, chunk, assemble, verify):
    if chunk:
        create_chunks(input_file)
    elif assemble:
        reassemble_chunks(input_file)
    elif verify:
        verify(input_file, output_file)

if __name__ == '__main__':
    main()