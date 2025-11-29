import sharp from 'sharp';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const targetDir = path.join(__dirname, 'public/images/watermark_remover');

console.log(`Scanning directory: ${targetDir}`);

if (!fs.existsSync(targetDir)) {
    console.error(`Directory not found: ${targetDir}`);
    process.exit(1);
}

fs.readdir(targetDir, (err, files) => {
    if (err) {
        console.error('Error reading directory:', err);
        return;
    }

    const imageFiles = files.filter(file => {
        const ext = path.extname(file).toLowerCase();
        return ext === '.png' || ext === '.jpg' || ext === '.jpeg';
    });

    console.log(`Found ${imageFiles.length} images to convert.`);

    imageFiles.forEach(file => {
        const ext = path.extname(file).toLowerCase();
        const inputFile = path.join(targetDir, file);
        const outputFile = path.join(targetDir, path.basename(file, ext) + '.webp');

        sharp(inputFile)
            .webp({ quality: 80 })
            .toFile(outputFile)
            .then(info => {
                console.log(`Converted ${file} to ${path.basename(outputFile)}`);
            })
            .catch(err => {
                console.error(`Error converting ${file}:`, err);
            });
    });
});

