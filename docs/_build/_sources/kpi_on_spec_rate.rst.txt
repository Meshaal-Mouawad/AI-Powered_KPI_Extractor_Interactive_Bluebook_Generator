kpi on spec rate
==================================================

.. math::

   \text{}

.. raw:: html

   <style>
      .kpi-table {
         width: 100%; border-collapse: collapse; margin-bottom: 1.5em;
         border: 1px solid #e0e0e0; table-layout: fixed;
      }
      .kpi-table td {
         padding: 12px; vertical-align: top; border: 1px solid #e0e0e0;
         word-wrap: break-word;
      }
      .kpi-table td:first-child {
         width: 25%; font-weight: bold; background-color: #f7f7f7;
      }
      .kpi-table ul { list-style-type: disc; padding-left: 20px; margin: 0; }
      .kpi-table .math-equation {
         text-align: center; margin: 1em 0; overflow-x: auto; padding: 5px;
      }
      .kpi-table .formula-notes li { margin-bottom: 0.5em; }
      .kpi-table .formula-notes i { font-family: 'Times New Roman', serif; }
      .btn { display:inline-block; padding:8px 12px; border-radius:6px; color:#fff; text-decoration:none; font-weight:500; font-size:13px; }
      .btn-vscode { background-color:#2c5282; }
      .btn-pycharm { background-color:#000; }
      .btn-edit { background-color:#4a7c59; }
   </style>

   <div style="margin-bottom: 1.5em; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 13px; font-weight: 500; color: #4a5568;">Open in:</span>
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/sql_kpi.sql:0" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/sql_kpi.sql&line=0" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=kpi%20on%20spec%20rate" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>The KPI on spec rate measures the percentage of batches produced that meet the specified quality standards within a given timeframe</li><li>This KPI expresses the proportion of production that meets all quality standards relative to total batches</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of this KPI is to ensure that production processes consistently yield high-quality products</li><li>thereby minimizing waste and enhancing customer satisfaction</li><li>Improve first-pass quality and reduce rework or off-spec material by monitoring on-spec performance over time</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>This KPI is calculated by taking the number of on-spec batches and dividing it by the total number of batches produced, then multiplying the result by 100 to express it as a percentage.</p>
               <p>See code context for implementation details.</p>
            </td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is utilized in quality control assessments and operational efficiency evaluations within the production process</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI include the count of on-spec batches and the total count of batches produced during the reporting period</li><li>Counts of on-spec batches and total batches in the measurement period</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for this KPI is percentage.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The data for this KPI is sourced from the batch quality summary database, which aggregates quality metrics from production.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A high on spec rate indicates effective quality control processes, while a low rate may signal the need for process improvements or additional training for staff.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   

      CREATE VIEW kpi_on_spec_rate AS
   SELECT
       CAST(100.0 * on_spec_batches / NULLIF(total_batches, 0) AS FLOAT) AS on_spec_percentage
   FROM batch_quality_summary;